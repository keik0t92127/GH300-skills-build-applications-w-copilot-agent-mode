import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
      const apiUrl = codespaceName
        ? `https://${codespaceName}-8000.app.github.dev/api/workouts/`
        : 'http://localhost:8000/api/workouts/';

      console.log('Fetching workouts from:', apiUrl);

      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Workouts API response:', data);
        
        // Handle both paginated (.results) and array formats
        const workoutsData = data.results || data;
        console.log('Processed workouts data:', workoutsData);
        
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      beginner: 'bg-success',
      intermediate: 'bg-warning',
      advanced: 'bg-danger'
    };
    return badges[difficulty] || 'bg-secondary';
  };

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center loading-message">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3">Loading workouts...</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4">💪 Suggested Workouts</h2>
      <p className="lead mb-4">Choose from our curated workout plans tailored to your fitness level.</p>
      <div className="row">
        {workouts.map((workout) => (
          <div key={workout.id} className="col-md-6 mb-4">
            <div className="card h-100 shadow-custom">
              <div className="card-header">
                <h5 className="card-title mb-0">{workout.name}</h5>
                <span className={`badge ${getDifficultyBadge(workout.difficulty)} mt-2`}>
                  {workout.difficulty.toUpperCase()}
                </span>
              </div>
              <div className="card-body">
                <p className="card-text">{workout.description}</p>
                <div className="mb-3">
                  <span className="badge bg-secondary">
                    <i className="bi bi-clock"></i> {workout.duration_minutes} minutes
                  </span>
                </div>
                <div>
                  <strong>Exercises:</strong>
                  <ul className="mt-2 list-group list-group-flush">
                    {workout.exercises?.map((exercise, index) => (
                      <li key={index} className="list-group-item px-0">
                        <i className="bi bi-check-circle text-success"></i> {exercise}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Workouts;
