"use client";

import { ChangeEvent, useState } from "react";
import { useRouter } from 'next/navigation';

export default function Home() {
  const [recipeLink, setRecipeLink] = useState("");
  const router = useRouter();

  function isLinkValid(message: string) {
    // Regular expression to match a valid URL
    const urlRegex = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/i;
    return urlRegex.test(message);
  }

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  const handleSubmission = async () => {
    if (recipeLink.trim() !== '') {
      // Check if the input is a valid link (you can use a regex or other validation logic here)
      if (isLinkValid(recipeLink)) {
        try {
          // Get the CSRF token from cookies
        const csrfToken = getCookie('csrftoken');

        // Make an API call with the recipeLink and CSRF token
        const data = { "link": recipeLink };
        const headers = {
          'Content-Type': 'application/json', // Adjust content type as necessary
          'X-CSRFToken': csrfToken, // Include the CSRF token in the headers
        };

          // Create the request object
          const request = {
            method: 'POST',
            headers: new Headers(headers),
            body: JSON.stringify(data), // Convert data to JSON string if sending JSON
          };

          const response = await fetch('http://127.0.0.1:8000/api/receive-url/', request);
          if (response.ok) {
            // API call was successful, navigate to the "virtual-chef" route
            router.push('/virtual-chef');
          } else {
            // Handle API errors
            console.error('API call failed');
          }
        } catch (error) {
          // Handle network errors
          console.error('Network error:', error);
        }
      } else {
        // Handle invalid link (e.g., show an error message to the user)
        console.error('Invalid link');
      }
    }
  };

  const handleRecipeLinkChange = (e: ChangeEvent<HTMLInputElement>) => {
    setRecipeLink(e.target.value);
  };
  return (
    <div className='flex flex-col justify-center'>
      <p className='text-slate-50 text-xl'>
        Please provide an Epicurious recipe link to your Virtual Chef:
      </p>
      <input
        className='rounded p-1 my-4'
        value={recipeLink}
        onChange={handleRecipeLinkChange}
      />
      <button type='submit' className='rounded bg-slate-400 p-1' onClick={handleSubmission}>
        Submit
      </button>
    </div>
  );
}
