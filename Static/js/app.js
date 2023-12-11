function init(){   
    console.log('init');
    d3.json(`/get_data_from_csv`).then((data) => {  
        console.table(data) 
    });
    d3.json(`/get_data_from_json`).then((data) => {  
        console.table(data) 
    });
};
init();