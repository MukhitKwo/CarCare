import React, { useState } from "react";

function App() {
  // State to track whether we're showing the Login form (true) or Register form (false)
  const [isLogin, setIsLogin] = useState(true);

  // Function to toggle between Login and Register forms
  const toggleForm = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {/* Show Login or Register form based on isLogin state */}
      {isLogin ? <Login /> : <Register />}

      {/* Button to switch between forms */}
      <button onClick={toggleForm} style={{ marginTop: "20px" }}>
        {isLogin ? "Go to Register" : "Go to Login"}
      </button>
    </div>
  );
}

function Login() {
  // Handle login form submission
  const handleLogin = (e) => {
    e.preventDefault(); // Prevent page reload
    alert("Logged in!"); // Replace with real login logic
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>Login</h2>
      <input type="text" placeholder="Username" required /><br /><br />
      <input type="password" placeholder="Password" required /><br /><br />
      <button type="submit">Login</button>
    </form>
  );
}

function Register() {
  // Handle registration form submission
  const handleRegister = (e) => {
    e.preventDefault(); // Prevent page reload
    alert("Registered!"); // Replace with real registration logic
  };

  return (
    <form onSubmit={handleRegister}>
      <h2>Register</h2>
      <input type="text" placeholder="Username" required /><br /><br />
      <input type="email" placeholder="Email" required /><br /><br />
      <input type="password" placeholder="Password" required /><br /><br />
      <button type="submit">Register</button>
    </form>
  );
}

export default App;
