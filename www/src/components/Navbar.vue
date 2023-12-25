<template>
  <div>
    <v-dialog v-model="dialogLogin" max-width="600px">
      <v-card rounded="xl">
        <v-card-text>
          <v-container>
            <v-col class="text-center pb-8 pt-8">
              <span class="demo-login">Demo</span
              ><span class="website">Website</span>
            </v-col>
            <v-row>
              <v-col cols="12" sm="12" md="12" lg="12" class="text-center">
                <v-text-field
                  label="Email"
                  hide-details=""
                  rounded
                  :rules="[rules.required, rules.email]"
                  v-model="username"
                  filled
                  color="#6a00a3"
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="12" md="12" lg="12" class="text-center">
                <v-text-field
                  label="Password"
                  hide-details=""
                  rounded
                  v-model="password"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show1 ? 'text' : 'password'"
                  filled
                  color="#6a00a3"
                  @click:append="show1 = !show1"
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="12" md="12" lg="12" class="text-center pt-6">
                <v-btn
                  rounded
                  elevation="0"
                  large
                  class="text-none"
                  color="#6a00a3"
                  dark
                  @click="login"
                  >Login</v-btn
                >
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogFail" width="400">
      <v-card
        class="text-center pl-16 pr-16 pt-8 pb-8"
        rounded="lg"
        elevation="0"
      >
        <v-avatar color="amber" size="70">
          <v-icon dark x-large>mdi-alert </v-icon>
        </v-avatar>
        <h2>Username or Password was wrong please try again</h2>
      </v-card>
    </v-dialog>
    <div class="nav-card">
      <v-container>
        <v-row>
          <v-col cols="6"
            ><span class="demo">Demo</span
            ><span class="website">Website</span></v-col
          >
          <v-col cols="6" class="text-right">
            <v-btn
              rounded
              elevation="0"
              color="#ffce00"
              class="text-none"
              @click="dialogLogin = true"
            >
              Login
            </v-btn>
          </v-col>
        </v-row>
        <v-row class="pt-16 pb-16 mb-16">
          <v-col cols="12" lg="6" md="6">
            <span class="discover">Discover the future of</span>
            <h1 class="demo-web">Demo Website</h1>
            <span class="lorem"
              >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Facere,
              quis natus cum ullam inventore et, suscipit officia sed, assumenda
              hic sapiente est? Eaque perferendis commodi ratione maiores
              beatae. Qui, maiores.</span
            >
          </v-col>
          <v-col cols="6" class="pa-16"> </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  components: {},
  data: () => ({
    username: "testuser",
    password: "testpassword",
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 4 || "Min 4 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },

    show1: false,
    valid: false,
    dialogLogin: false,
    dialogFail: false,
  }),
  watch: {
    dialogFail(val) {
      if (!val) return;

      setTimeout(() => (this.dialogFail = false), 3000);
    },
  },
  methods: {
    login() {
      let data = {
        username: this.username,
        password: this.password,
      };

      axios
        .post(`http://localhost:4000/token`, data)
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            localStorage.setItem("token", response.data.access_token);

            this.dialogLogin = false;
            this.$router.push("/dashboard");
          } else {
            this.dialogFail = true;
          }
        })
        .catch((e) => {
          this.dialogFail = true;

          console.log(e);
        });
    },
  },
};
</script>
