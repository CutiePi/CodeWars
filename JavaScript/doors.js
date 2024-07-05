// 3 door problem


const doorp = () => {
    const randomIndex = Math.floor(Math.random() * 3);
    const randomChoiceIndex = Math.floor(Math.random() * 3);
    const doors = [false, false, false];
    doors[randomIndex] = true;
    const choice1 = doors.slice(randomChoiceIndex,randomChoiceIndex+1);
    const firstFreeGoatIndex = doors.findIndex((v,i ) => !v && i!==randomChoiceIndex);
    const choice2 = 3 - (randomChoiceIndex + firstFreeGoatIndex);
    return [choice1[0], doors[choice2]];
 }

 let areyawinnngson = 0;
let areyalosingson = 0;
 for(let i = 0;i<42069;i++){
    const r = doorp();
     if(r[0]) areyawinnngson++;
     if(r[1]) areyalosingson++;
 }

 console.log("Standaroo", areyawinnngson);
 console.log("Switchroo", areyalosingson);