<template>
  <view class="login">
    <input v-model="username" placeholder="请输入用户名" />
    <input v-model="password" type="password" placeholder="请输入密码" />
    <button @click="handleLogin">登录</button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async handleLogin() {
      try {
        if (!this.username || !this.password) {
          console.error('用户名或密码不能为空');
          return;
        }
        const response = await this.$request('/auth/login', 'POST', {
          username: this.username,
          password: this.password,
        });
        console.log('登录成功', response);
		// uni.showModal({
		//   title: '登录成功',
		//   content: '这是一个简单的弹窗',
		//   success: (res) => {
		//     if (res.confirm) {
		//       console.log('用户点击了确定');
		//     } else if (res.cancel) {
		//       console.log('用户点击了取消');
		//     }
		//   }
		// });
		// uni.showToast({
		//   title: '操作成功',
		//   icon: 'success', // 可选值：'success'、'loading'、'none'
		//   duration: 2000 // 显示时长
		// });
        // uni.navigateTo({ url: '/pages/user-manage/user-manage' });
		// uni.switchTab({ url: '/pages/user-manage/user-manage' });
		// 优先级： uni.navigateTo > uni.showModal ,uni.showToast
      } catch (err) {
        console.error('登录失败', err);
      }
    },
  },
};
</script>