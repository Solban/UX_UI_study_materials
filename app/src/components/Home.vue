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
            <button class="previous-btn" @click="previous"><i class="material-icons">keyboard_arrow_left</i> Previous</button>
            <button class="next-btn" @click="next">Next <i class="material-icons">keyboard_arrow_right</i></button>
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
        category: this.$route.params['category'],
        examples: examples[this.$route.params['category']]
      }
    },
    mounted() {
      let id = this.$route.params['id'];
      if (id) {
        this.examples = [examples[this.$route.params['category']][id]]
      }
    },
    methods: {
        next() {
          this.active++;
          if (this.examples.length === this.active) {
            this.active = 0;
          }
          this.showCorrect = false;
        },
      previous() {
        this.active--;
        if (this.active === -1) {
          this.active = this.examples.length - 1;
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

    button {
        height: 40px;
        border: none;
        width: 150px;
        font-size: 16px;
        cursor: pointer;
    }

    button:focus {
        outline: none;
    }

    button.previous-btn {
        float: left;
        margin-left: 15px;
        background: #ddd;
    }

    button.previous-btn:hover {
        background: #d2d2d2;
    }

    button.next-btn {
        float: right;
        margin-right: 15px;
        background: #F62459;
        color: #fff;
    }

    button.next-btn:hover {
        background: #e52357;
    }

    button.next-btn .material-icons {
        color: #fff;
    }
</style>
