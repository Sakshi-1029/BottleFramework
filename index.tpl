<!DOCTYPE html>
<html>
<head>
    <title>File List</title>
</head>
<body>
    <h1>File List</h1>
    <table>
        <thead>
            <tr>
                <th>File Name</th>
                <th>File Size (bytes)</th>
            </tr>
        </thead>
        <tbody>
            % for file in file_list:
                <tr>
                    <td>{{ file[0] }}</td>
                    <td>{{ file[1] }}</td>

                </tr>
            % end
        </tbody>
    </table>
</body>
</html>