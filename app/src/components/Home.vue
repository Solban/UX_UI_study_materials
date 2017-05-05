<template>
    <div class="content">
        <div class="container">
            <h1>Which UX is good?</h1>
            <div class="examples">
                <div class="example" @click="showCorrect = true">
                    <img :src="examples[0].image1">
                    <div class="correct" v-if="showCorrect && examples[0].correct === 0">Do</div>
                    <div class="incorrect" v-if="showCorrect && examples[0].correct !== 0">Don't</div>
                    <div class="explanation" v-if="showCorrect">{{ examples[0].explanation1 }}</div>
                </div><div class="example" @click="showCorrect = true">
                    <img :src="examples[0].image2">
                    <div class="correct" v-if="showCorrect && examples[0].correct === 1">Do</div>
                    <div class="incorrect" v-if="showCorrect && examples[0].correct !== 1">Don't</div>
                    <div class="explanation" v-if="showCorrect">{{ examples[0].explanation2 }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        showCorrect: false,
        examples: [
          {
            image1: 'https://storage.googleapis.com/material-design/publish/material_v_11/assets/0BxFyKV4eeNjDb3BRZzNaT2R2V1E/style_color_uiapplication_accent3.png',
            image2: 'https://storage.googleapis.com/material-design/publish/material_v_11/assets/0BxFyKV4eeNjDNGw2OGFydndWQTA/style_color_uiapplication_accent4.png',
            explanation1: 'Use a secondary color for certain text, such as linked text.',
            explanation2: 'Don’t use bright colors for body text, even if your primary or secondary colors are bright.',
            correct: 0
          },
          {
            image1: 'https://storage.googleapis.com/material-design/publish/material_v_11/assets/0Bzhp5Z4wHba3b1BpT0dRd0tFaUE/components_bottomsheets_modal_do.png',
            image2: 'https://storage.googleapis.com/material-design/publish/material_v_11/assets/0Bzhp5Z4wHba3UTB0bG8tYWxVRG8/components_bottomsheets_modal_dont.png',
            explanation1: '',
            explanation2: '',
            correct: 0
          }
        ]
      }
    },
    methods: {

    }
  }
</script>

<style lang="scss">
    .content {
        width: calc(100% - 250px);
        margin-left: 250px;
    }

    .container {
        width: 100%;
    }

    .examples {
        width: 800px;
        margin: 0 auto;
    }

    .example {
        width: 400px;
        display: inline-block;
        cursor: pointer;
        padding: 20px;
    }

    .example img {
        max-width: 100%;
        max-height: 500px;
        border-bottom: 5px solid transparent;
    }

    .example img:hover {
        background: #aaa;
        border-bottom: 5px solid #aaa;
    }

    .example.left {
        text-align: right;
    }

    .correct, .incorrect {
        width: 100%;
        text-transform: uppercase;
        text-align: left;
        padding: 5px 0 0 0;
        font-weight: 700;
        font-size: 14px;
    }

    .correct {
        border-top: 5px solid green;
        color: green;
    }

    .incorrect {
        border-top: 5px solid red;
        color: red;
    }

    .explanation {
        width: 100%;
        margin: 15px 0;
        text-align: left;
    }
</style>
