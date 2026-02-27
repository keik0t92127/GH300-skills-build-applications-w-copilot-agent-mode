import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
      const apiUrl = codespaceName
        ? `https://${codespaceName}-8000.app.github.dev/api/leaderboard/`
        : 'http://localhost:8000/api/leaderboard/';

      console.log('Fetching leaderboard from:', apiUrl);

      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Leaderboard API response:', data);
        
        // Handle both paginated (.results) and array formats
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard data:', leaderboardData);
        
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center loading-message">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3">Loading leaderboard...</p>
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
      <h2 className="mb-4">🏆 Leaderboard</h2>
      <p className="lead mb-4">Compete and track your fitness rankings!</p>
      <div className="table-responsive">
        <table className="table table-striped table-hover align-middle">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Username</th>
              <th>Total Activities</th>
              <th>Total Duration (min)</th>
              <th>Total Calories</th>
              <th>Last Updated</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((entry) => (
              <tr key={entry.id} className={entry.rank <= 3 ? 'table-warning' : ''}>
                <td>
                  {entry.rank === 1 && <span className="badge bg-warning text-dark me-2">🥇</span>}
                  {entry.rank === 2 && <span className="badge bg-secondary me-2">🥈</span>}
                  {entry.rank === 3 && <span className="badge bg-warning text-dark me-2">🥉</span>}
                  <strong className={entry.rank <= 3 ? 'text-warning fw-bold' : ''}>
                    #{entry.rank}
                  </strong>
                </td>
                <td>{entry.username}</td>
                <td>{entry.total_activities}</td>
                <td>{entry.total_duration_minutes}</td>
                <td>{entry.total_calories_burned.toFixed(1)}</td>
                <td>{new Date(entry.updated_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
