<template>
    <div class="wrapper">
        <papercontent></papercontent>
        <commentscontent></commentscontent>
    </div>
</template>

<script>
import papercontent from './PaperPage.vue';
import commentscontent from './CommentsPage.vue';

export default {
    data() {
        return {
        };
    },
    components: {
        papercontent,
        commentscontent
    },
};
</script>

