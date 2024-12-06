// frontend/src/App.tsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import FAQPage from "./pages/FAQPage";
// import Layout from "./components/Layout";

const App = () => {
  return (
    <Router>
      {/* <Layout> */}
      <Routes>
        <Route path="/" element={<FAQPage />} />
      </Routes>
      {/* </Layout> */}
    </Router>
  );
};

export default App;
