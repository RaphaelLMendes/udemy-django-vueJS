<template>
    <div class="card col-sm-6 mx-2" style="width: 18rem;">
        <img src="https://image.api.playstation.com/vulcan/img/rnd/202011/0714/vuF88yWPSnDfmFJVTyNJpVwW.png" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">
                <slot name="title">not working</slot>
            </h5>
            <p class="card-text">
                <slot name="description">description 1</slot>
            </p>
            <a href="#" class="btn btn-primary">{{ msg }}</a>
        </div>
    </div>
</template>

<script>
export default {
data() {
    return {
        
    }
},
props : {
        msg : String
    }
}
</script>