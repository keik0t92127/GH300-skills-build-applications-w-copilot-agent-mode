import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
      const apiUrl = codespaceName
        ? `https://${codespaceName}-8000.app.github.dev/api/teams/`
        : 'http://localhost:8000/api/teams/';

      console.log('Fetching teams from:', apiUrl);

      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Teams API response:', data);
        
        // Handle both paginated (.results) and array formats
        const teamsData = data.results || data;
        console.log('Processed teams data:', teamsData);
        
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching teams:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center loading-message">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3">Loading teams...</p>
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
      <h2 className="mb-4">🏆 Teams</h2>
      <p className="lead mb-4">Total Teams: <span className="badge bg-success">{teams.length}</span></p>
      <div className="row">
        {teams.map((team) => (
          <div key={team.id} className="col-md-6 mb-4">
            <div className="card h-100 shadow-custom">
              <div className="card-header bg-primary text-white">
                <h5 className="card-title mb-0">{team.name}</h5>
              </div>
              <div className="card-body">
                <p className="card-text">{team.description}</p>
              </div>
              <div className="card-footer bg-transparent">
                <small className="text-muted">
                  <i className="bi bi-calendar"></i> Created: {new Date(team.created_at).toLocaleDateString()}
                </small>
                <br />
                <small className="text-muted">
                  <i className="bi bi-people"></i> Members: <span className="badge bg-info">{team.members?.length || 0}</span>
                </small>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Teams;
