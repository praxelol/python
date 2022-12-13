// Define the dimensions of the UI
var w = 1920;
var h = 1080;

// Create a new solid layer and set its dimensio

var bg = comp.layers.addSolid([0,0,0], "Background", w, h, 1);

// Create a new shape layer and add it to the composition
var shape = comp.layers.addShape();
shape.name = "Twitter UI";
shape.moveToEnd();

// Add a rectangle to the shape layer
var rect = shape.content.addProperty("ADBE Vector Shape - Rect");
rect.property("Size").setValue([w,h]);
rect.property("Position").setValue([w/2,h/2]);

// Set the fill color of the rectangle
var fill = shape.content.addProperty("ADBE Vector Graphic - Fill");
fill.property("Color").setValue([0.5,0.5,0.5]);

// Add a rounded rectangle to the shape layer
var rounded = shape.content.addProperty("ADBE Vector Shape - Rounded Corners");
rounded.property("Size").setValue([300,100]);
rounded.property("Position").setValue([w/2,h/2]);
rounded.property("Roundness").setValue(20);

// Set the fill color of the rounded rectangle
var fill2 = shape.content.addProperty("ADBE Vector Graphic - Fill");
fill2.property("Color").setValue([0.8,0.8,0.8]);

// Add a text layer to the composition
var text = comp.layers.addText("Twitter");
text.name = "Logo";
text.moveToEnd();

// Set the font and text size of the text layer
var textProp = text.property("Source Text");
textProp.setValue("Twitter");
textProp.property("Font").setValue("Helvetica");
textProp.property("FontSize").setValue(30);

// Set the position and color of the text layer
text.property("Position").setValue([w/2,h/2]);
text.property("Fill Color").setValue([0,0,0]);
