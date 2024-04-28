"use state"
import React, { useState } from "react";
import { FaTimes } from "react-icons/fa";

const CreateTMYKModal = () => {
  return (
    <>
      <div className="fixed z-10 inset-0">
        <div className="flex items-center justify-center min-h-screen">
          <div className="bg-white rounded-lg p-8 max-w-3xl w-full">
            <h2 className="text-2xl font-bold mb-4">This is your modal</h2>
            <p>You can put whatever content you want here.</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default CreateTMYKModal;
