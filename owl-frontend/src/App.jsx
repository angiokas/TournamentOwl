import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { pages } from "./data/pages";
import PageLayout from "./components/PageLayout";

function App() {
  return (
    <>
      <Router>
        <PageLayout pages={pages}>
          <Routes>
            {pages.map((page) => (
              <Route
                key={page.name}
                path={page.route}
                element={page.component}
              />
            ))}
          </Routes>
        </PageLayout>
      </Router>
    </>
  );
}

export default App;
