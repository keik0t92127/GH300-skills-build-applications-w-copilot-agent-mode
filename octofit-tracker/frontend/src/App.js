import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Teams from './components/Teams';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              🏋️ OctoFit Tracker
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    Users
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    Leaderboard
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    Workouts
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route
            path="/"
            element={
              <div className="container mt-4">
                <div className="jumbotron text-center">
                  <h1 className="display-4 text-gradient">Welcome to OctoFit Tracker! 🏋️‍♂️</h1>
                  <p className="lead mt-3">
                    Track your fitness journey with our comprehensive fitness tracking application.
                  </p>
                  <hr className="my-4" />
                  <p className="mb-4">Navigate using the menu above to explore:</p>
                  <div className="row mt-4">
                    <div className="col-md-4 mb-3">
                      <div className="card h-100 shadow-custom">
                        <div className="card-body text-center">
                          <h3 className="card-title">👥</h3>
                          <h5 className="card-title">Users</h5>
                          <p className="card-text">View all registered users and their profiles.</p>
                          <Link to="/users" className="btn btn-primary">View Users</Link>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-4 mb-3">
                      <div className="card h-100 shadow-custom">
                        <div className="card-body text-center">
                          <h3 className="card-title">🏆</h3>
                          <h5 className="card-title">Teams</h5>
                          <p className="card-text">See team information (Marvel vs DC!).</p>
                          <Link to="/teams" className="btn btn-success">View Teams</Link>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-4 mb-3">
                      <div className="card h-100 shadow-custom">
                        <div className="card-body text-center">
                          <h3 className="card-title">🏃</h3>
                          <h5 className="card-title">Activities</h5>
                          <p className="card-text">Browse workout activities and logs.</p>
                          <Link to="/activities" className="btn btn-info">View Activities</Link>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="row mt-3">
                    <div className="col-md-6 mb-3">
                      <div className="card h-100 shadow-custom">
                        <div className="card-body text-center">
                          <h3 className="card-title">🏆</h3>
                          <h5 className="card-title">Leaderboard</h5>
                          <p className="card-text">Check rankings and competitive stats.</p>
                          <Link to="/leaderboard" className="btn btn-warning">View Leaderboard</Link>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-6 mb-3">
                      <div className="card h-100 shadow-custom">
                        <div className="card-body text-center">
                          <h3 className="card-title">💪</h3>
                          <h5 className="card-title">Workouts</h5>
                          <p className="card-text">Get suggested workout routines.</p>
                          <Link to="/workouts" className="btn btn-danger">View Workouts</Link>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            }
          />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

