import React from "react";
import { useTable } from "react-table";

function Table() {
    const data = React.useMemo(
        () => [
            {
                rank: 1,
                username: "player1",
                title: "GM",
                rating: 2800,
                country: "Country1",
            },
            {
                rank: 2,
                username: "player2",
                title: "GM",
                rating: 2750,
                country: "Country2",
            },
            {
                rank: 3,
                username: "player3",
                title: "IM",
                rating: 2650,
                country: "Country3",
            },
            {
                rank: 4,
                username: "player4",
                title: "FM",
                rating: 2550,
                country: "Country4",
            },
            {
                rank: 5,
                username: "player5",
                title: "FM",
                rating: 2500,
                country: "Country5",
            },
            // Add more dummy data as needed...
        ],
        []
    );

    const columns = React.useMemo(
        () => [
            { Header: "Rank", accessor: "rank" },
            { Header: "Username", accessor: "username" },
            { Header: "Title", accessor: "title" },
            { Header: "Rating", accessor: "rating" },
            { Header: "Country", accessor: "country" },
        ],
        []
    );

    const tableInstance = useTable({ columns, data });

    const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
        tableInstance;

    return (
        <table {...getTableProps()} className="table-auto border-collapse border border-gray-400">
            <thead>
                {headerGroups.map((headerGroup) => (
                    <tr key={headerGroup.id} {...headerGroup.getHeaderGroupProps()} className="bg-gray-200">
                        {headerGroup.headers.map((column) => (
                            <th key={column.id} {...column.getHeaderProps()} className="px-4 py-2 font-bold">
                                {column.render("Header")}
                            </th>
                        ))}
                    </tr>
                ))}
            </thead>
            <tbody {...getTableBodyProps()}>
                {rows.map((row) => {
                    prepareRow(row);
                    return (
                        <tr key={row.id} {...row.getRowProps()} className="hover:bg-gray-100">
                            {row.cells.map((cell) => (
                                <td key={cell.id} {...cell.getCellProps()} className="border px-4 py-2 font-bold">
                                    {cell.render("Cell")}
                                </td>
                            ))}
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
}

export default Table;
