// import React from "react";
import { GoogleLogin } from "react-google-login";

const clientID ="274864533718 - mjphgjqd1ht0ar20b0r1f5ds47n0po55.apps.googleusercontent.com";

function login() {
  const onSuccess = (res) => {
    console.log("Login Success: currentUser:", res.profileObj);
  };
  const onFaliure = (res) => {
    console.log("Login Failed: res:", res);
  };
  return (
    <div id="signInButton">
      <GoogleLogin
        clientID={clientID}
        buttonTex="Login"
        onSuccess={onSuccess}
        onFaliure={onFaliure}
        cokkiePolicy={"single_host_origin"}
        isSignedIn={true}
      />
    </div>
  );
}

export default login;
