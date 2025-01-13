<template>
	<view class="user-manage">
		<input v-model="username" placeholder="请输入用户名" />
		<input v-model="password" type="password" placeholder="请输入密码" />
		<button @click="createUser">新增用户</button>
		
		<view v-for="user in users" :key="user.id" class="user-item">
			<text>{{ user.username }}</text>
			<button @click="deleteUser(user.id)">删除</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				users: [],
				username: '',
				password: '',
			};
		},
		methods: {
			async fetchUsers() {
				const response = await this.$request('/users', 'GET');
				this.users = response;
			},
			async createUser() {
				try {
					if (this.username && this.password) {
						const response = await this.$request('/users/create', 'POST', {
							username: this.username,
							password: this.password,
						});
						this.users.push(response);
						console.log('用户创建成功', response);
					} else {
						console.error('用户名或密码不能为空');
					}
				} catch (err) {
					console.error('用户创建失败', err);
				}
			},
			async deleteUser(id) {
				try {
					await this.$request(`/users/${id}`, 'DELETE');
					this.users = this.users.filter((user) => user.id !== id);
				} catch (err) {
					console.error('删除失败', err);
				}
			},
		},
		onLoad() {
			this.fetchUsers();
		},
	};
</script>