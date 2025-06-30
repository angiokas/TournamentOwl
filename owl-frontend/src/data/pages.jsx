import HomePage from "../pages/HomePage";
import TournamentsPage from "../pages/TournamentsPage";
import JudgesPage from "../pages/JudgesPage";
import ParticipantsPage from "../pages/ParticipantsPage";
import ResourcesPage from "../pages/ResourcesPage";
import RegistrationPage from "../pages/RegistrationPage";

export const pages = [
  { name: "home", title: "Home", route: "/", component: <HomePage /> },
  {
    name: "tournaments",
    title: "Tournaments",
    route: "/tournaments",
    component: <TournamentsPage />,
  },
  {
    name: "resources",
    title: "Resources",
    route: "/resources",
    component: <ResourcesPage />,
  },
  {
    name: "participants",
    title: "For Participants",
    route: "/participants",
    component: <ParticipantsPage />,
  },
  {
    name: "judges",
    title: "For Judges",
    route: "/judges",
    component: <JudgesPage />,
  },
  {
    name: "registration",
    title: "Registration",
    route: "registration",
    component: <RegistrationPage />,
  },
];
