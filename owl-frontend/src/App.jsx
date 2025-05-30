import React from "react";
import NavigationBar from "./components/NavigationBar";
import BottomBar from "./components/BottomBar";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TournamentsPage from "./pages/TournamentsPage";
import JudgesPage from "./pages/JudgesPage";
import ParticipantsPage from "./pages/ParticipantsPage";
import ResourcesPage from "./pages/ResourcesPage";

const pages = [
  { name: "home", title: "Home", route: "/", component: HomePage },
  {
    name: "tournaments",
    title: "Tournaments",
    route: "/tournaments",
    component: TournamentsPage,
  },
  {
    name: "resources",
    title: "Resources",
    route: "/resources",
    component: ResourcesPage,
  },
  {
    name: "participants",
    title: "For Participants",
    route: "/for-participants",
    component: ParticipantsPage,
  },
  {
    name: "judges",
    title: "For Judges",
    route: "/for-judges",
    component: JudgesPage,
  },
];

function App() {
  return (
    <>
      <Router>
        <NavigationBar pages={pages} />
        <Routes>
          {pages.map(({ route, component, name }, index) => (
            <Route
              key={index}
              path={route}
              element={React.createElement(component)}
            />
          ))}
        </Routes>
        <BottomBar />
      </Router>
    </>
  );
}

export default App;
