<template>
    <div class="container">
        <el-row :gutter="30">
            <el-col :span="24">
                <el-input placeholder="Search for a specialist" v-model="keyword" class="specialist-filter">
                    <el-button slot="append" icon="el-icon-search" @click="getSpecialists"></el-button>
                </el-input>
            </el-col>
        </el-row>
        <el-row :gutter="30" class="specialists">
            <el-col :span="specialist ? 18 : 24">
                <el-divider content-position="left">Specialists</el-divider>
                <el-col v-for="item in specialists" :span="6">
                    <div class="specialist-mini" @click="showSpecialist(item)">
                        <el-card>
                            <p>{{ item.user__name }}</p>
                            <p><el-tag size="mini">{{ item.title }}</el-tag></p>
                        </el-card>
                    </div>
                </el-col>
            </el-col>
            <el-col v-if="specialist" :span="6" class="specialist-large">
                <el-card>
                    <div class="header">
                        <p>Name: {{ specialist.user__name }}</p>
                        <p>Title: {{ specialist.title }}</p>
                    </div>
                    <h3>Make an appointment</h3>
                    <el-form :model="appointment" ref="appointment" label-width="120px" label-position="top">
                        <el-form-item label="Title" prop="title" required>
                            <el-input v-model="appointment.title"></el-input>
                        </el-form-item>
                        <el-form-item label="Date and time" required>
                            <el-date-picker type="datetime" placeholder="Pick a date and time" v-model="appointment.date"
                                            style="width: 100%;"></el-date-picker>
                        </el-form-item>
                        <el-form-item label="Notes" prop="notes" required>
                            <el-input type="textarea" v-model="appointment.notes"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="bookAppoinment">Confirm</el-button>
                            <el-button @click="clearAppointment">Cancel</el-button>
                        </el-form-item>
                    </el-form>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                keyword: '',
                specialists: [],
                specialist: null,
                appointmentUrl: 'activity/appointment',
                specialistsUrl: 'account/search?keyword=',
                appointment: {
                    title: '',
                    notes: '',
                    date: ''
                }
            }
        },
        methods: {
            getSpecialists: function () {
                axios.get(`${this.specialistsUrl}${this.keyword}`).then((response) => {
                    this.specialists = response.data.result;
                });
            },
            showSpecialist: function (item) {
                this.specialist = item;
            },
            bookAppoinment: function () {
                this.appointment.specialist = this.specialist.id;
                axios.post(this.appointmentUrl, this.appointment).then((response) => {
                    if (response.data.success) {
                        this.$message.success('Your appointment has been booked');
                        this.clearAppointment();
                    } else {
                        this.$message.error('An error occurred. Please try again');
                    }
                }).catch(() => this.$message.error('An error occurred. Please try again'));
            },
            clearAppointment: function () {
                this.$refs['appointment'].resetFields();
            }
        },
        mounted() {
            this.getSpecialists();
        }
    }
</script>

<style>
    .specialist-input .el-input-group__prepend {
        background-color: #fff;
    }
    .specialists {
        padding-top: 1em;
    }
    .specialist-mini {
        cursor: pointer;
    }
    .specialist-large .header, h3 {
        text-align: center;
    }
</style>