import './App.css';
import Dashboard from './components/Dashboard';
import Navbar from './components/Navbar';
import Table from './components/Table';
import Login from './components/login';
import Logout from './components/logout';
import { useEffect, useState } from 'react';
import {gapi}  from 'gapi-script';

const clientID =  "274864533718 - mjphgjqd1ht0ar20b0r1f5ds47n0po55.apps.googleusercontent.com";


function App() {
  const [showDashboard, setShowDashboard] = useState(false);

  useEffect(()=>{
    function start(){
      gapi.client.init({
        clientID: clientID,
        scope: ""
      })
    }
    gapi.load('client:auth2', start);
  })
  return (
    <>
      <div>
        
        <Navbar />
        <Table />
        <Login/>
        <Logout/>
        <button
          onClick={() => setShowDashboard(!showDashboard)}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-auto my-4 flex"
          style={{ margin: '1rem 0' }}
        >
          Show Dashboard
        </button>
        {showDashboard ? <Dashboard /> : null}
      </div>
    </>
  );
}

export default App;

