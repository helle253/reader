import host from './host.js';

//
// Tries to get the token pair from the cookie.
//
// Returns nothing if cookie is invalid or not present.
//
// @returns Promise<{access_token: string, refresh_token: string} | undefined>
export default async function () {
  const cookie = await chrome.cookies.get({url: host, name: "tokenPair"});
  if (cookie && cookie.value) {
    try {
      return JSON.parse(cookie.value);
    } catch (e) {
      console.error("Error parsing tokenPair cookie.");
    }
  }
}
