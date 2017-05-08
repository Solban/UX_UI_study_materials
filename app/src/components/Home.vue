<template>
    <div class="content">
        <div class="container">
            <h1>Which UX is good?</h1>
            <div class="examples">
                <div class="example left" @click="showCorrect = true">
                    <img :src="examples[active].img1">
                </div><div class="example" @click="showCorrect = true">
                    <img :src="examples[active].img2">
                </div>
                <div class="example left">
                    <div class="correct" v-if="showCorrect">Do</div>
                    <div class="explanation" v-if="showCorrect">{{ examples[active].img1_text }}</div>
                </div><div class="example">
                    <div class="incorrect" v-if="showCorrect">Don't</div>
                    <div class="explanation" v-if="showCorrect">{{ examples[active].img2_text }}</div>
                </div>
                <div class="explanation full" v-if="showCorrect && examples[active].description !== ''"><i class="material-icons">lightbulb_outline</i> {{ examples[active].description }}</div>
            </div>
            <button @click="next">Next example</button>
        </div>
    </div>
</template>

<script>
  import examples from '../examples';

  export default {
    name: 'home',
    data () {
      return {
        showCorrect: false,
        active: 0,
        category: 'Button',
        examples: examples['Button']
      }
    },
    mounted() {
      let category = this.$route.params['category'];
      if (category) {
        this.category = category;
        this.examples = examples[category];
      }
    },
    methods: {
        next() {
          this.active++;
          if (this.examples.length === this.active) {
            this.active = 0;
          }
          this.showCorrect = false;
        }
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
        text-align: right;
    }

    .explanation {
        width: 100%;
        margin: 15px 0;
        text-align: left;
    }

    .explanation.full {
        line-height: 30px;
    }

    .explanation .material-icons {
        height: 30px;
        width: 30px;
        background: #f9e72e;
        color: #f5f5f5;
        line-height: 30px;
        text-align: center;
        border-radius: 50%;
        margin-right: 5px;
    }
</style>
