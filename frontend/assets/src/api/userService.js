import { http } from './http.js';
import { tokenManager } from './tokenManager.js';

export const userService = {
  async login(credentials) {
    const data = await http('/auth/login', {
      method: 'POST',
      body: JSON.stringify(credentials),
    });

    tokenManager.setAccessToken(data.access);
    tokenManager.setRefreshToken(data.refresh);
    return data.user;
  },

  async getProfile() {
    return http('/user/profile');
  },

  async updateProfile(profileData) {
    return http('/user/profile', {
      method: 'PUT',
      body: JSON.stringify(profileData),
    });
  },

  async logout() {
    tokenManager.clear();
  },
};