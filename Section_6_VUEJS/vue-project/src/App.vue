<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from '@/components/HelloWorld.vue'
import TheNavBar from '@/components/TheNavBar.vue'
</script>

<template>
    <header>
      <TheNavBar />
    </header>

  <div class="container">
    <RouterView />
  </div>
</template>

<style>
</style>
