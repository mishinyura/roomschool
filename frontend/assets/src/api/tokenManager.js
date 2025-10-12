export const tokenManager = {
  getAccessToken() {
    return localStorage.getItem('access_token');
  },
  setAccessToken(token) {
    localStorage.setItem('access_token', token);
  },
  removeAccessToken() {
    localStorage.removeItem('access_token');
  },

  getRefreshToken() {
    return localStorage.getItem('refresh_token');
  },
  setRefreshToken(token) {
    localStorage.setItem('refresh_token', token);
  },
  removeRefreshToken() {
    localStorage.removeItem('refresh_token');
  },

  clear() {
    this.removeAccessToken();
    this.removeRefreshToken();
  },
};