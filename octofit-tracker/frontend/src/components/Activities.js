import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
      const apiUrl = codespaceName
        ? `https://${codespaceName}-8000.app.github.dev/api/activities/`
        : 'http://localhost:8000/api/activities/';

      console.log('Fetching activities from:', apiUrl);

      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Activities API response:', data);
        
        // Handle both paginated (.results) and array formats
        const activitiesData = data.results || data;
        console.log('Processed activities data:', activitiesData);
        
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching activities:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  const getActivityBadgeClass = (activityType) => {
    const badges = {
      running: 'bg-primary',
      cycling: 'bg-info',
      swimming: 'bg-cyan',
      weightlifting: 'bg-danger',
      yoga: 'bg-success'
    };
    return badges[activityType] || 'bg-secondary';
  };

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center loading-message">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3">Loading activities...</p>
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
      <h2 className="mb-4">🏃 Activities</h2>
      <p className="lead mb-4">Total Activities: <span className="badge bg-info">{activities.length}</span></p>
      <div className="table-responsive">
        <table className="table table-striped table-hover align-middle">
          <thead>
            <tr>
              <th>User</th>
              <th>Activity Type</th>
              <th>Duration (min)</th>
              <th>Calories</th>
              <th>Distance (km)</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity) => (
              <tr key={activity.id}>
                <td><strong>{activity.user_id}</strong></td>
                <td>
                  <span className={`badge ${getActivityBadgeClass(activity.activity_type)}`}>
                    {activity.activity_type}
                  </span>
                </td>
                <td><span className="badge bg-secondary">{activity.duration_minutes} min</span></td>
                <td><span className="badge bg-warning text-dark">{activity.calories_burned.toFixed(1)} cal</span></td>
                <td>{activity.distance_km ? `${activity.distance_km.toFixed(2)} km` : 'N/A'}</td>
                <td>{new Date(activity.created_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
