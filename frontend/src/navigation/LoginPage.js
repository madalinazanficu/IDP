import React from 'react';
import './LoginPage.css';

const LoginPage = ({ history }) => {
  const handleLogin = () => {
    // Simulate login logic, for example, you might validate credentials here
    // and then redirect to home page
    history.push('/home');
  };

  return (
    <div className="login-page-container">
      <h2 className="login-header">Login Page</h2>
      <button className="login-button" onClick={handleLogin}>Login</button>
    </div>
  );
};

export default LoginPage;