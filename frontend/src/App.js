import './App.css';
import { Route, Routes } from "react-router-dom";
import HomePage from './pages/Home';
import LoginPage from './pages/Login';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/blabla" elemnt={<HomePage></HomePage>} />
        <Route path="/home" element={<HomePage></HomePage>} />
      </Routes>
    </div>
  );
}

export default App;
