// import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-green-500 text-black">
      <div className="flex items-center justify-between">
        <h1 className="m-0 p-4 text-xl font-bold">Chess-Base</h1>
        <ul className="flex">
          <li className="mr-4">
            <a href="/" className="hover:text-gray-200">Home</a>
          </li>
          <li className="mr-4">
            <a href="/about" className="hover:text-gray-200">About Us</a>
          </li>
          <li>
            <a href="/things" className="hover:text-gray-200">Things</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};


export default Navbar;
