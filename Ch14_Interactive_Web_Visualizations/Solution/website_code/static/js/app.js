var data = {};

d3.json("./samples.json").then(function (input_data) {
    console.log(input_data);
    // save to global variable
    data = input_data; 

    makeDropdown();
    makeBarChart("940");
    makeMetaTable("940");
    makeBubbles("940");
});


function makeDropdown() {
    for (let i = 0; i < data.names.length; i++){
        let name = data.names[i];
        d3.select("#selDataset").append("option").text(name);
    }
}

function optionChanged(val) {
    makeBarChart(val);
    makeMetaTable(val);
    makeBubbles(val);
}

function makeBarChart(val) {
  let new_data = data.samples.filter(x => x.id === val)[0];

    let trace1 = {
        x: new_data.sample_values.slice(0, 10).reverse(),
        y: new_data.otu_ids.slice(0, 10).reverse().map(x => `OTU ID: ${x}`),
        name: "Bacteria",
        type: "bar",
        orientation: "h",
        marker: {
            color: "rgb(158,202,225)",
            opacity: 0.6,
            line: {
                color: "rgb(8,48,107)",
                width: 1.5
            }
        },
        hovertext: new_data.otu_labels
    };

    let traces = [trace1];

    let layout = {
        title: "Bacteria Bar Chart",
        yaxis: {
            tickangle: -25
        }
    };

    Plotly.newPlot("bar", traces, layout);
}


function makeMetaTable(val) {
    let new_data = data.metadata.filter(x => x.id == val)[0];
    console.log(new_data);
    d3.select("#sample-metadata").html("");

    Object.entries(new_data).forEach(function (key) {
        d3.select("#sample-metadata").append("h6").text(`${key[0]}: ${key[1]}`);
    });
}


function makeBubbles(val) {
    let new_data = data.samples.filter(x => x.id === val)[0];

    let trace1 = {
        x: new_data.otu_ids,
        y: new_data.sample_values,
        name: "Bacteria",
        mode: "markers",
        marker: {
            color: new_data.otu_ids,
            colorscale: "Electric",
            size: new_data.sample_values
        },
        hovertext: new_data.otu_labels
    };

    let traces = [trace1];

    let layout = {title: "Bacteria Bubbles"};

    Plotly.newPlot("bubble", traces, layout);
}