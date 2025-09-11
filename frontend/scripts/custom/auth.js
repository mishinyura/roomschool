const AuthApp = {
    data() {
        return {
            loader: false,
            title: 'Авторизация',
            roles: [
                // {
                //     name: 'admin',
                //     display: 'Администратор'
                // },
                // {
                //     name: 'employee',
                //     display: 'Сотрудник'
                // },
                // {
                //     name: 'parent',
                //     display: 'Родитель'
                // }
            ],
            login: '',
            password: ''
        }
    },
    methods: {
        async auth() {
            let response = await fetch(
                'https://testium-app-default-rtdb.firebaseio.com/users.json',
                {
                    method: 'GET',
                    // headers: {
                    //     'Content-Type': 'application/json'
                    // },
                    // body: JSON.stringify({
                    //     login
                    // })
                }
            )
            
            let result = await response.json()
            this.roles.push(result.slice(1))

            console.log(this.roles)
            return result
        }
    }
}

Vue.createApp(AuthApp).mount('#auth')