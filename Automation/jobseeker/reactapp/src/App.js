import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
//import { Routes, Route } from 'react-router-dom';

// Import components
import Home from "./Home";
import About from "./About";
import Blog from "./Blog";

import "./styles.css";

const App = () => (
  <Router>
    <div className="nav-bar">
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/blog">Blog</Link>
    </div>
    <Routes>
      {/* Exact match to avoid 
          overriding other routes */}
      <Route path="/" exact>
        <Home />
      </Route>
      <Route path="/about">
        <About />
      </Route>
      <Route path="/blog">
        <Blog />
      </Route>
    </Routes>
  </Router>
);

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);