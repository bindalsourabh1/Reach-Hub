// import React from 'react'

import { GoogleLogout } from "react-google-login";

const clientID =
  "274864533718 - mjphgjqd1ht0ar20b0r1f5ds47n0po55.apps.googleusercontent.com";
function logout() {
  const onSuccess = () => {
    console.log("Logout Successfull");
    // alert("Logout Successfull ✌");
  };
  return (
    <div>
      <GoogleLogout
        clientID={clientID}
        buttonText={"Logout"}
        onLogoutSuccess={onSuccess} 
      />
    </div>
  );
}

export default logout;
