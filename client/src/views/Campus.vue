<script>
import Sidebar from '../components/Sidebar.vue';
import CampusHeader from '../components/CampusHeader.vue';

export default {
  name: 'Campus',
  components: {
    CampusHeader,
    Sidebar
  }
}
</script>

<template>
    <div class="">
      <CampusHeader />  
      <Sidebar />
        <main class="main-content-area">
          <router-view></router-view>
        </main>
    </div>
</template>

<style scoped>
</style>