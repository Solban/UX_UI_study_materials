<template>
    <div class="content">
        <div class="container">
            <h1>Which UI is good?</h1>
            <div class="examples">
                <div class="example left" @click="showCorrect = true">
                    <img :class="{hideCorrect: !showCorrect}" :src="left.img">
                </div><div class="example" @click="showCorrect = true">
                    <img :class="{hideCorrect: !showCorrect}" :src="right.img">
                </div>
                <div class="example left">
                    <div class="correct" v-if="showCorrect && examples[active].img1 === left.img">Do</div>
                    <div class="incorrect" v-if="showCorrect && examples[active].img1 !== left.img">Don't</div>
                    <div class="explanation" v-if="showCorrect">{{ left.img_text }}</div>
                </div><div class="example">
                    <div class="correct" v-if="showCorrect && examples[active].img1 === right.img">Do</div>
                    <div class="incorrect" v-if="showCorrect && examples[active].img1 !== right.img">Don't</div>
                    <div class="explanation" v-if="showCorrect">{{ right.img_text }}</div>
                </div>
                <div class="explanation full" v-if="showCorrect && examples[active].description !== ''"><i class="material-icons">lightbulb_outline</i> <p>{{ examples[active].description }}</p></div>
                <button class="previous-btn" @click="previous"><i class="material-icons">keyboard_arrow_left</i> Previous</button>
                <button class="next-btn" @click="next">Next <i class="material-icons">keyboard_arrow_right</i></button>
            </div>
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
        examples: examples[this.$route.params['category']],
        left: {img: "", img_text: ""},
        right: {img: "", img_text: ""}
      }
    },
    mounted() {
      let id = this.$route.params['id'];
      if (id) {
        this.examples = [examples[this.$route.params['category']][id]]
      }
      this.randomize();
      let _this = this;
      document.onkeydown = function(e) {
        if (e.keyCode === 39) {
          _this.next();
        } else if (e.keyCode === 37) {
          _this.previous();
        }
      }
    },
    methods: {
      randomize() {
        let example = this.examples[this.active];
        let min = 1;
        let max = 2;
        let random = Math.floor(Math.random() * (max - min + 1)) + min;
        if (random === 1) {
          this.left = {
            img: example.img1,
            img_text: example.img1_text
          };
          this.right = {
            img: example.img2,
            img_text: example.img2_text
          }
        } else {
          this.right = {
            img: example.img1,
            img_text: example.img1_text
          };
          this.left = {
            img: example.img2,
            img_text: example.img2_text
          }
        }
      },
      next() {
        this.active++;
        if (this.examples.length === this.active) {
          this.active = 0;
        }
        this.showCorrect = false;
        this.randomize();
      },
      previous() {
        this.active--;
        if (this.active === -1) {
          this.active = this.examples.length - 1;
        }
        this.showCorrect = false;
        this.randomize();
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
        width: 1200px;
        margin: 0 auto;
        padding-bottom: 60px;
    }

    .example {
        width: 600px;
        display: inline-block;
        cursor: pointer;
        padding: 20px;
    }

    .example img {
        max-width: 100%;
        max-height: 600px;
        border: 5px solid transparent;
    }

    .example img.hideCorrect:hover {
        border: none;
    }

    .example.left {
        text-align: right;
    }

    .example.left .correct, .example.left .incorrect {
        text-align: left;
    }

    .correct, .incorrect {
        width: 100%;
        text-transform: uppercase;
        padding: 5px 0 0 0;
        font-weight: 700;
        font-size: 14px;
        text-align: right;
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

    .explanation.full {
        line-height: 30px;
        margin: 15px 15px 50px 15px;
    }

    .explanation .material-icons {
        height: 30px;
        width: 30px;
        background: #f9e72e;
        color: #f5f5f5;
        line-height: 30px;
        text-align: center;
        border-radius: 50%;
        margin-right: 10px;
        display: inline-block;
    }

    .explanation p {
        display: inline-block;
        width: calc(100% - 45px);
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
