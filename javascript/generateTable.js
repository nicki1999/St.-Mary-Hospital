export function generateTable(rows, columns) {
    // Get the HTML element where we want to append the table
    const tableContainer = document.getElementById('table-container');
  
    // Create a new table element
    const table = document.createElement('table');
  
    // Create the first row and merge all the cells
    const titleRow = document.createElement('tr');
    const titleCell = document.createElement('td');
    titleCell.setAttribute('colspan', columns * 3);
    titleCell.style.textAlign = 'center'; // Center the text
    const titleText = document.createTextNode('Table Title');
    const boldText = document.createElement('strong'); // Create a <strong> element
    boldText.appendChild(titleText);
    titleCell.appendChild(boldText);
    titleRow.appendChild(titleCell);
    table.appendChild(titleRow);
  
    // Create the second row with n cells
    const secondRow = document.createElement('tr'); 
    for (let j = 0; j < columns; j++) {
      const cell = document.createElement('td');
      cell.setAttribute('colspan',columns);
      cell.style.textAlign = 'center';
      const cellText = document.createTextNode(`Row 2, Column ${j+1}`);
      cell.appendChild(cellText);
      secondRow.appendChild(cell);
    }
    table.appendChild(secondRow);
  
    // Loop through the rows starting from the third row
    for (let i = 2; i < rows; i++) {
      // Create a new row element
      const row = document.createElement('tr');
  
      // Loop through the columns * 3
      for (let j = 0; j < columns * 3; j++) {
        // Create a new cell element
        const cell = document.createElement('td');
        
        // Add some text to the cell
        const cellText = document.createTextNode(`Row ${i+1}, Column ${j+1}`);
        cell.appendChild(cellText);
  
        // Add the cell to the row
        row.appendChild(cell);
      }
  
      // Add the row to the table
      table.appendChild(row);
    }
  
    // Add the table to the container
    tableContainer.appendChild(table);
  }