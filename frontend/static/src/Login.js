import React, {Component} from 'react';
import axios from 'axios';

  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';

  class Login extends Component {
    login = (e) => {
      e.preventDefault();

      let user = {
        username: 'admin',
        email: 'admin@example.com',
        password: 'safepass1'
      }

      axios.post('/api/v1/rest-auth/login/', user)
      .then(res => {
        console.log(res);
        localStorage.setItem("my-app-key", res.data.key)
      })
      .catch(error => {
        console.log(error)
      });
    }
    render() {
      return(
      <form onSubmit={this.handleSubmit}>
        <button>Login</button>
      </form>
    )
    }
  }
