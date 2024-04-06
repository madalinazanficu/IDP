import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import LoginPage from './navigation/LoginPage';
import HomePage from './navigation/HomePage';

function App() {
  return (
    <Router>
      <div>
        <Route exact path="/" component={LoginPage} />
        <Route path="/home" component={HomePage} />
      </div>
    </Router>
  );
}

export default App;