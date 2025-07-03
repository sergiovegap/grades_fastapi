<script>
export default {
  name: 'CampusHeader',
  computed: {
    headerTitle() {
      const matched = this.$route.matched.find(record => record.meta && record.meta.headerTitle);
      return matched ? matched.meta.headerTitle : 'Online School';
    }
  }
}
</script>

<template>
    <header class="header-container">
        <div class="header-content">
            <div>
                <p>{{ headerTitle }}</p>
            </div>
            <div class="header-icons">
                <div>
                    <p>Header</p>
                </div>
                <div>
                    <p>Header</p>
                </div>
                <div>
                    <p>Header</p>
                </div>
            </div>
        </div>
    </header>
</template>

<style scoped>
</style>