const dayjs = require("dayjs");


const birthday = (data) =>{
    let day = dayjs(data);
    const age = dayjs().diff(day,'years');
    console.log("You have: " + age +" years");
    const nextBirth = day.add(age + 1, "Years");
    console.log("Your next birthday will: " + nextBirth.format("DD/MM/YYYY") +  " in a " + nextBirth.format("dddd"));
    console.log(`Missing ${nextBirth.diff(dayjs(),'days')}  days for your next birthday`)

};

birthday("1999-10-25");