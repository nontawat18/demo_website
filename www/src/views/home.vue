<template>
  <div>
    <Navbar />
    <v-dialog v-model="dialog" max-width="600px">
      <v-card rounded="xl">
        <v-card-title>
          <span class="text-h5">EXPLORE OUR JOB OPPORTUNITIES </span>
        </v-card-title>
        <v-card-subtitle
          >Discover all the open positions and find the one that suits you
          best.</v-card-subtitle
        >

        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  label="Frist Name"
                  hide-details=""
                  rounded
                  :rules="rules.required"
                  v-model="firstname"
                  filled
                  color="#6a00a3"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  rounded
                  filled
                  :rules="rules.required"
                  v-model="lastname"
                  color="#6a00a3"
                  label="Last Name"
                  hide-details=""
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  rounded
                  filled
                  :rules="rules.required"
                  v-model="age"
                  color="#6a00a3"
                  label="Age"
                  hide-details=""
                  type="number"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  label="Email"
                  hide-details=""
                  rounded
                  :rules="[rules.required, rules.email]"
                  v-model="email"
                  filled
                  color="#6a00a3"
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  label="Phone"
                  hide-details=""
                  type="number"
                  rounded
                  :rules="rules.required"
                  v-model="phone"
                  filled
                  color="#6a00a3"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  label="Position"
                  hide-details=""
                  rounded
                  filled
                  :rules="rules.required"
                  v-model="position"
                  color="#6a00a3"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  label="Current Salary"
                  hide-details=""
                  type="number"
                  rounded
                  :rules="rules.required"
                  v-model="currentSalary"
                  filled
                  color="#6a00a3"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="6" lg="6">
                <v-text-field
                  label="Expected Salary"
                  hide-details=""
                  type="number"
                  rounded
                  filled
                  :rules="rules.required"
                  v-model="expectedSalary"
                  color="#6a00a3"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12" md="12" lg="12">
                <v-textarea
                  rounded
                  filled
                  :rules="rules.required"
                  v-model="address"
                  color="#6a00a3"
                  label="Address"
                  hide-details=""
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions class="pb-4">
          <v-spacer></v-spacer>
          <v-btn color="#6b00a3" class="text-none" text @click="submitWork">
            Submit
          </v-btn>

          <v-btn color="error" class="text-none" text @click="dialog = false">
            Cancle
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogFinish" width="300">
      <v-card
        class="text-center pl-16 pr-16 pt-8 pb-8"
        rounded="lg"
        elevation="0"
      >
        <v-avatar color="#6a00a3" size="70">
          <v-icon dark x-large>mdi-check </v-icon>
        </v-avatar>
        <h2>Submit Success!</h2>
      </v-card>
    </v-dialog>
    <v-container>
      <v-row justify="center" class="card-all">
        <v-col
          cols="12"
          lg="3"
          md="3"
          v-for="(item, i) in card"
          :key="i"
          class="pa-4"
        >
          <v-badge :content="i + 1" :value="i + 1" color="#ffce00" overlap left>
            <v-card class="pa-6" rounded="xl" elevation="5">
              <v-icon color="#6b00a3" size="85">
                {{ item.icon }}
              </v-icon>
              <h2 class="text-card">{{ item.text }}</h2>
            </v-card>
          </v-badge>
        </v-col>
      </v-row>
      <v-row class="pb-16" align="center">
        <v-col cols="12" lg="5" md="5">
          <v-img :src="require('../assets/img/work.png')"> </v-img>
        </v-col>
        <v-col cols="12" lg="7" md="7">
          <span class="demo-work-with-us">Demo Website</span>
          <h1 class="work-with-us">Work with us</h1>
          <span class="demo-span">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure
            maiores ea ad deleniti dolorum vitae, eum qui cum accusamus natus
            architecto velit aperiam quasi labore unde, consectetur tenetur
            optio sed?
          </span>
          <br />
          <br />
          <span class="demo-span">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure
            maiores ea ad deleniti dolorum vitae, eum qui cum accusamus natus
            architecto velit aperiam quasi labore unde, consectetur tenetur
            optio sed?
          </span>
          <v-col class="pt-12 pl-0">
            <v-btn
              rounded
              elevation="0"
              large
              class="text-none"
              color="#6a00a3"
              dark
              @click="dialog = true"
              >Submit Work</v-btn
            >
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import Navbar from "../components/Navbar.vue";
import logo from "../assets/img/check.png";
import axios from "axios";
import moment from "moment";
import { format, parseISO } from "date-fns";
export default {
  components: {
    Navbar,
    logo,
  },
  data: () => ({
    card: [
      {
        icon: "mdi-web",
        text: "Lorem ipsum dolor, sit amet consectetur adipisicing elit.",
      },
      {
        icon: "mdi-share-variant",
        text: "Lorem ipsum dolor, sit amet consectetur adipisicing elit.",
      },
      {
        icon: "mdi-equalizer-outline",
        text: "Lorem ipsum dolor, sit amet consectetur adipisicing elit.",
      },
    ],
    dialog: false,
    files: [],
    dialogFinish: false,
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 4 || "Min 4 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },
    firstname: "",
    lastname: "",
    age: 0,
    email: "",
    phone: "",
    position: "",
    currentSalary: "",
    expectedSalary: "",
    address: "",
    date: format(parseISO(new Date().toISOString()), "yyyy-MM-dd"),
  }),
  watch: {
    dialogFinish(val) {
      if (!val) return;

      setTimeout(() => (this.dialogFinish = false), 4000);
    },
  },
  methods: {
    generateThumbnail(file) {
      let fileSrc = URL.createObjectURL(file);
      setTimeout(() => {
        URL.revokeObjectURL(fileSrc);
      }, 1000);
      return fileSrc;
    },
    makeName(name) {
      return (
        name.split(".")[0].substring(0, 3) +
        "..." +
        name.split(".")[name.split(".").length - 1]
      );
    },

    remove(i) {
      // this.files.splice(i, 1)
      this.files = [];
    },
    onChange() {
      console.log(this.$refs.file.files);
      this.files = [...this.$refs.file.files];
    },
    uploadFile(e) {
      this.files = e.target.files;
      console.log(this.files);
      this.base64 = e.target.files;
    },

    dragover(e) {
      e.preventDefault();
      this.isDragging = true;
    },

    dragleave() {
      this.isDragging = false;
    },

    drop(e) {
      e.preventDefault();
      this.$refs.file.files = e.dataTransfer.files;
      this.onChange();
      this.isDragging = false;
    },
    submitWork() {
      let data = {
        id: 0,
        firstname: this.firstname,
        lastname: this.lastname,
        age: this.age,
        email: this.email,
        phone: this.phone,
        position: this.position,
        currentSalary: this.currentSalary,
        expectedSalary: this.expectedSalary,
        address: this.address,
        dateSubmit: this.date,
        status: "pending",
      };

      axios
        .post(`http://localhost:4000/submit-work/`, data)
        .then((response) => {
          console.log(response);
          this.dialog = false;
          this.dialogFinish = true;
          window.location.reload();
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
