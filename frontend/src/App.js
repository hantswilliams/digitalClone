import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/login/Login";
import Register from "./components/register/Register";
import Reset from "./components/reset/Reset";
import Dashboard from "./components/dashboard/Dashboard";
import Clone from "./components/clone/Clone";
import Page from "./navigation/Page";

function App() {
  return (
    <div className="app">
      <Router>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route exact path="/register" element={<Register />} />
          <Route exact path="/reset" element={<Reset />} />
          <Route exact path="/dashboard" element={<Dashboard />} />
          <Route exact path="/clone" element={<Clone />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;



// import React from "react";
// // import { BrowserRouter, Route, Switch } from "react-router-dom";
// import "./App.css";
// import Page from "./navigation/Page";

// const App = ({ pageroutes }) => (
//   // We use <BrowserRouter> in order to support
//   // routing example hosted on GitHub pages.
//   // <BrowserRouter> could be safely replaced with <Router> in
//   // your production application.
//   <Router>
//     <Routes>
//       {pageroutes.map(route => (
//         <Route key={route.path} path={route.path}>
//           <Page route={route} />
//         </Route>
//       ))}
//     </Routes>
//   </Router>
// );

// export default App;