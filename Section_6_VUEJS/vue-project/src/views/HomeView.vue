<script setup>
import TheFilmCard from '@/components/TheFilmCard.vue'
</script>

<template>
  <main>
    <div class="py-5">
      <div class="row">
        <TheFilmCard v-for="(film, index) in films" :key="index" :msg="film.title">
          <template v-slot:title>
            {{ film.title }}
          </template>
          <template v-slot:description>
            {{ film.description }}
          </template>
        </TheFilmCard>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      films: [
        {
          title: "test 1",
          description:"Description 1",
        },
        {
          title: "test 2",
          description:"Description 2",
        },
        {
          title: "test 3",
          description:"Description 3",
        }
      ]
    }
  }
}
</script>
