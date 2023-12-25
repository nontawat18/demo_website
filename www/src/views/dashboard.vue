<template>
  <div>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-col class="text-center">
        <span class="demo-login">Demo</span><span class="website">Website</span>
      </v-col>

      <v-divider></v-divider>
      <v-col>
        <v-list>
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            router
            exact
            color="#680001"
            @click="list(item.to)"
          >
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app color="#ffffff" elevation="0">
      <div class="btn align-center">
        <v-btn
          icon
          @click.stop="miniVariant = !miniVariant"
          x-small
          elevation="0"
          dark
        >
          <v-icon>mdi-{{ `chevron-${miniVariant ? "right" : "left"}` }}</v-icon>
        </v-btn>
      </div>
    </v-app-bar>
    <div class="pt-8">
      <!-- <v-container> -->
      <v-col class="pb-8">
        <v-row class="pa-0" align="center">
          <v-col cols="12" lg="8" md="8" class="pa-0"> </v-col>

          <v-col cols="11" lg="3" md="3">
            <v-menu
              v-model="menu1"
              :close-on-content-click="false"
              max-width="290"
              offset-y
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  rounded
                  filled
                  hide-details=""
                  :rules="[rules.required, rules.email]"
                  color="#6a00a3"
                  :value="computedDateFormattedMomentjs"
                  append-icon="mdi-calendar-outline"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                no-title
                color="#6a00a3"
                v-model="date"
                locale="th-TH"
                @change="menu1 = false"
              ></v-date-picker>
            </v-menu>
          </v-col>
          <v-col cols="1" lg="1" md="1" class="pa-0">
            <v-btn elevation="0" fab color="#6a00a3" dark @click="sortTable">
              <v-icon>mdi-magnify</v-icon></v-btn
            >
          </v-col>
        </v-row>
      </v-col>

      <v-col>
        <v-row justify="center">
          <v-col
            cols="12"
            lg="3"
            md="3"
            v-for="(item, i) in cards"
            :key="i"
            class="pa-4"
          >
            <v-card
              dark
              rounded="xl"
              elevation="0"
              class="pa-6"
              :color="item.color"
            >
              <v-col class="text-center">
                <h1>{{ sumPerDay[i].length }}</h1>
                <small>{{ item.text }}</small>
              </v-col>
            </v-card>
          </v-col>
        </v-row>
      </v-col>

      <v-col class="">
        <v-data-table
          :headers="headers"
          :items="people"
          sort-by="calories"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title class="pl-2"
                ><h2>List of people who applied for jobs</h2>
              </v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn
                color="green"
                dark
                class="text-none mb-2 mr-2"
                @click="exportFile"
              >
                <v-icon left>mdi-file-excel</v-icon>
                Export CSV
              </v-btn>
              <v-dialog v-model="dialog" max-width="600px">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="#2da4da"
                    dark
                    class="text-none mb-2"
                    v-bind="attrs"
                    v-on="on"
                  >
                    New Applied
                  </v-btn>
                </template>
                <v-card>
                  <v-card-title>
                    <span class="text-h5">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            label="Frist Name"
                            hide-details=""
                            v-model="editedItem.firstname"
                            rounded
                            filled
                            color="#6a00a3"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            rounded
                            v-model="editedItem.lastname"
                            filled
                            color="#6a00a3"
                            label="Last Name"
                            hide-details=""
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            rounded
                            filled
                            v-model="editedItem.age"
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
                            v-model="editedItem.email"
                            filled
                            color="#6a00a3"
                          ></v-text-field>
                        </v-col>

                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            label="Phone"
                            hide-details=""
                            type="number"
                            v-model="editedItem.phone"
                            rounded
                            filled
                            color="#6a00a3"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            label="Position"
                            v-model="editedItem.position"
                            hide-details=""
                            rounded
                            filled
                            color="#6a00a3"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            label="Current Salary"
                            v-model="editedItem.currentSalary"
                            hide-details=""
                            type="number"
                            rounded
                            filled
                            color="#6a00a3"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="6" md="6" lg="6">
                          <v-text-field
                            label="Expected Salary"
                            v-model="editedItem.expectedSalary"
                            hide-details=""
                            type="number"
                            rounded
                            filled
                            color="#6a00a3"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="12" md="12" lg="12">
                          <v-select
                            label="Status"
                            v-model="editedItem.status"
                            hide-details=""
                            rounded
                            filled
                            :items="status"
                            color="#6a00a3"
                          ></v-select>
                        </v-col>
                        <v-col cols="12" sm="12" md="12" lg="12">
                          <v-textarea
                            rounded
                            filled
                            v-model="editedItem.address"
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
                    <v-btn color="#6b00a3" class="text-none" text @click="save">
                      Submit
                    </v-btn>

                    <v-btn color="error" class="text-none" text @click="close">
                      Cancle
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
              <v-dialog v-model="dialogDelete" max-width="500px">
                <v-card>
                  <v-card-title class="text-h5"
                    ><strong>Are you sure you want to delete</strong>
                    <strong style="color: red"
                      >{{ editedItem.firstname }}
                      {{ editedItem.lastname }}</strong
                    ></v-card-title
                  >
                  <v-card-actions>
                    <v-spacer></v-spacer>

                    <v-btn color="#6a00a3" text @click="deleteItemConfirm"
                      >OK</v-btn
                    ><v-btn color="error" text @click="closeDelete"
                      >Cancel</v-btn
                    >
                    <v-spacer></v-spacer>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)" color="#2da4da">
              mdi-pencil
            </v-icon>
            <v-icon small @click="deleteItem(item)" color="error">
              mdi-delete
            </v-icon>
          </template>
          <template v-slot:[`item.firstname`]="{ item }">
            <span>{{ item.firstname }} {{ item.lastname }}</span>
          </template>
          <template v-slot:[`item.status`]="{ item }">
            <v-chip
              class="ma-2"
              dark
              color="error"
              v-if="item.status == 'pending'"
            >
              Pending
            </v-chip>
            <v-chip
              class="ma-2"
              dark
              color="amber"
              v-else-if="item.status == 'interview'"
            >
              Interview
            </v-chip>
            <v-chip
              class="ma-2"
              color="light-blue"
              dark
              v-else-if="item.status == 'test'"
            >
              Test
            </v-chip>
            <v-chip class="ma-2" dark color="#00E676" v-else> Confirm </v-chip>
          </template>
        </v-data-table>
      </v-col>
      <!-- </v-container> -->
    </div>
  </div>
</template>
<script>
import axios from "axios";
import moment from "moment";
import { format, parseISO } from "date-fns";
export default {
  name: "DefaultLayout",
  data() {
    return {
      cards: [
        {
          icon: "mdi-web",
          text: "Pending",
          color: "error",
        },
        {
          icon: "mdi-share-variant",
          text: "Interview",
          color: "amber",
        },
        {
          icon: "mdi-equalizer-outline",
          text: "Test",
          color: "light-blue",
        },
        {
          icon: "mdi-equalizer-outline",
          text: "Confirm",
          color: "#00E676",
        },
      ],
      clipped: false,
      drawer: true,
      fixed: false,
      items: [
        {
          icon: "mdi-account-multiple",
          title: "People applied jobs",
          to: "/dashboard",
        },
        {
          icon: "mdi-logout",
          title: "Logout",
          to: "/",
        },
        // {
        //   icon: 'mdi-chart-bubble',
        //   title: 'Inspire',
        //   to: '/inspire',
        // },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Vuetify.js",
      dialog: false,
      dialogDelete: false,
      files: [],
      people: [],
      headers: [
        {
          text: "Full Name",
          align: "start",
          sortable: false,
          value: "firstname",
        },
        { text: "Email", value: "email" },
        { text: "Position", value: "position" },
        { text: "Address", value: "address" },
        { text: "Status", value: "status" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      status: ["pending", "interview", "test", "confirm"],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        id: 0,
        firstname: "",
        lastname: "",
        age: "",
        email: "",
        phone: "",
        position: "",
        currentSalary: "",
        expectedSalary: "",
        address: "",
        dateSubmit: "",
        status: "",
      },
      defaultItem: {
        id: 0,
        firstname: "",
        lastname: "",
        age: "",
        email: "",
        phone: "",
        position: "",
        currentSalary: "",
        expectedSalary: "",
        address: "",
        dateSubmit: "",
        status: "",
      },
      date: format(parseISO(new Date().toISOString()), "yyyy-MM-dd"),
      menu1: false,
      rules: {
        required: (value) => !!value || "Required.",
        min: (v) => v.length >= 4 || "Min 4 characters",
        emailMatch: () => `The email and password you entered don't match`,
      },
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    computedDateFormattedMomentjs() {
      moment.locale("th");

      return this.date ? moment(this.date).format(`DD MMMM YYYY`) : "";
    },

    sumName() {
      let statusName = [];
      this.people.forEach((item, i) => {
        if (statusName.indexOf(this.people[i].status) < 0)
          statusName.push(this.people[i].status);
        return statusName;
      });
      console.log("statusName 1", statusName);

      return statusName;
    },
    sumPerDay: {
      get() {
        if (
          this.status == null ||
          this.status == 0 ||
          this.status == [] ||
          this.status == ""
        ) {
          return null;
        } else {
          let list = [];
          this.status.forEach((item) => {
            if (this.people == null) {
            } else {
              var aquaticCreatures = this.people.filter(function (creature) {
                return creature.status == item;
              });
              list.push(aquaticCreatures);
              return list;
            }
          });
          console.log(list);
          return list;
        }
      },
      set() {},
    },
  },
  mounted() {
    if (
      localStorage.getItem("token") == "null" ||
      localStorage.getItem("token") == ""
    ) {
      this.$router.push("/");

      console.log(localStorage.getItem("token"));
    }
    this.getData();
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  methods: {
    getData() {
      axios
        .get(`http://localhost:4000/get-all/`)
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            this.people = response.data;
            console.log(response.data);
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
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

    editItem(item) {
      this.editedIndex = this.people.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.people.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      axios
        .delete(`http://localhost:4000/submit-work/${this.editedItem.id}`)
        .then((response) => {
          console.log(response);
          this.getData();
        })
        .catch((e) => {
          console.log(e);
        });
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        // Object.assign(this.people[this.editedIndex], this.editedItem);
        let data = {
          id: this.editedItem.id,
          firstname: this.editedItem.firstname,
          lastname: this.editedItem.lastname,
          age: this.editedItem.age,
          email: this.editedItem.email,
          phone: this.editedItem.phone,
          position: this.editedItem.position,
          currentSalary: this.editedItem.currentSalary,
          expectedSalary: this.editedItem.expectedSalary,
          address: this.editedItem.address,
          dateSubmit: this.date,
          status: this.editedItem.status,
        };

        axios
          .put(`http://localhost:4000/update-work/${this.editedItem.id}`, data)
          .then((response) => {
            console.log(response);
            this.getData();
          })
          .catch((e) => {
            console.log(e);
          });
      } else {
        let data = {
          id: 0,
          firstname: this.editedItem.firstname,
          lastname: this.editedItem.lastname,
          age: this.editedItem.age,
          email: this.editedItem.email,
          phone: this.editedItem.phone,
          position: this.editedItem.position,
          currentSalary: this.editedItem.currentSalary,
          expectedSalary: this.editedItem.expectedSalary,
          address: this.editedItem.address,
          dateSubmit: this.date,
          status: this.editedItem.status,
        };

        axios
          .post(`http://localhost:4000/submit-work/`, data)
          .then((response) => {
            console.log(response);
            this.getData();
          })
          .catch((e) => {
            console.log(e);
          });
      }
      this.close();
    },
    async exportFile() {
      const response = await fetch(`http://localhost:4000/export/csv/`);
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);

      const a = document.createElement("a");
      a.href = url;
      a.download = "data.csv";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    },
    list(link) {
      if (link == "/dashboard") {
        this.$router.push("/dashboard");
      } else {
        localStorage.setItem("token", null);
        this.$router.push("/");
      }
    },
    sortTable() {
      axios
        .get(`http://localhost:4000/submit-work/${this.date}`)
        .then((response) => {
          console.log(response);
          if (response.status == 200) {
            this.people = response.data;
            console.log(response.data);
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>
<style lang="scss">
.v-btn:not(.v-btn--round).v-size--default {
  height: 36px;
  min-width: 64px;
  padding: 0 16px;
}
</style>
