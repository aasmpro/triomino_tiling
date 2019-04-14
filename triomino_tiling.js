function solve(n, key) {
    var square_size = 2 ** n;
    var table = {};
    for (var row = 0; row < square_size; row++) {
        for (var column = 0; column < square_size; column++) {
            table[[row, column]] = [0, false];
        }
    }
    table[key] = [1, true];
    recursive_solve([0, square_size - 1], [0, square_size - 1], square_size, table);
    return table
}

function recursive_solve(rows, columns, square_size, table) {
    if (rows[1] - rows[0] === 1) {
        if (table[[rows[0], columns[0]]][1]) {
            table[[rows[0], columns[1]]][0] = 200;
            table[[rows[1], columns[0]]][0] = 201;
            table[[rows[1], columns[1]]][0] = 202;
        } else if (table[[rows[0], columns[1]]][1]) {
            table[[rows[0], columns[0]]][0] = 210;
            table[[rows[1], columns[0]]][0] = 211;
            table[[rows[1], columns[1]]][0] = 212;
        } else if (table[[rows[1], columns[0]]][1]) {
            table[[rows[0], columns[0]]][0] = 220;
            table[[rows[0], columns[1]]][0] = 221;
            table[[rows[1], columns[1]]][0] = 222;
        } else if (table[[rows[1], columns[1]]][1]) {
            table[[rows[0], columns[0]]][0] = 230;
            table[[rows[0], columns[1]]][0] = 231;
            table[[rows[1], columns[0]]][0] = 232;
        }
        return
    }
    var max_row_number = rows[1];
    var min_row_number = rows[0];
    var max_column_number = columns[1];
    var min_column_number = columns[0];
    var sub_max_row = min_row_number + Math.floor((max_row_number - min_row_number) / 2);
    var sub_min_row = sub_max_row + 1;
    var sub_max_column = min_column_number + Math.floor((max_column_number - min_column_number) / 2);
    var sub_min_column = sub_max_column + 1;
    var f1 = false;
    var f2 = false;
    var f3 = false;
    var f4 = false;

    for (var row = min_row_number; row <= max_row_number; row++) {
        for (var column = min_column_number; column <= max_column_number; column++) {
            if (row <= sub_max_row && column <= sub_max_column) {
                if (table[[row, column]][1]) {
                    f1 = true
                }
            } else if (row <= sub_max_row && column > sub_max_column) {
                if (table[[row, column]][1]) {
                    f2 = true
                }
            } else if (row > sub_max_row && column <= sub_max_column) {
                if (table[[row, column]][1]) {
                    f3 = true
                }
            } else if (row > sub_max_row && column > sub_max_column) {
                if (table[[row, column]][1]) {
                    f4 = true
                }
            }
        }
    }

    if (f1) {
        table[[sub_max_row, sub_min_column]] = [200, true];
        table[[sub_min_row, sub_max_column]] = [201, true];
        table[[sub_min_row, sub_min_column]] = [202, true];
    } else if (f2) {
        table[[sub_max_row, sub_max_column]] = [210, true];
        table[[sub_min_row, sub_max_column]] = [211, true];
        table[[sub_min_row, sub_min_column]] = [212, true];
    } else if (f3) {
        table[[sub_max_row, sub_max_column]] = [220, true];
        table[[sub_max_row, sub_min_column]] = [221, true];
        table[[sub_min_row, sub_min_column]] = [222, true];
    } else if (f4) {
        table[[sub_max_row, sub_max_column]] = [230, true];
        table[[sub_max_row, sub_min_column]] = [231, true];
        table[[sub_min_row, sub_max_column]] = [232, true];
    }

    recursive_solve([min_row_number, sub_max_row], [min_column_number, sub_max_column], square_size, table);
    recursive_solve([min_row_number, sub_max_row], [sub_min_column, max_column_number], square_size, table);
    recursive_solve([sub_min_row, max_row_number], [min_column_number, sub_max_column], square_size, table);
    recursive_solve([sub_min_row, max_row_number], [sub_min_column, max_column_number], square_size, table);
}