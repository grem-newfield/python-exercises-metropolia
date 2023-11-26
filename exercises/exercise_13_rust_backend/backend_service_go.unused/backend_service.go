package main

import (
	"database/sql"
	"fmt"
	"log"
	// "net/http"
  // "encoding/json"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
  get_airport()
	// http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// fmt.Fprintf(w, "Hello, world!")
	// })
	// http.ListenAndServe(":5000", nil)
}

//  returns the name and location of the airport in JSON format. The
//  information is fetched from the airport database used on this course. For
//  example, the GET request for EFHK would be:
//  `http://127.0.0.1:5000/airport/EFHK`. The response must be in the format
//  of:

// {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}

func get_airport(icao: string) {
	connStr := "db_user:thereisaspoon@/test"

	db, err := sql.Open("mysql", connStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	rows, err := db.Query("SELECT id, name, municipality FROM airport WHERE gps_code = \"%s\"", icao)
	if err != nil {
		log.Fatal(err)
	}

	for rows.Next() {
		var icao, name, municipality string

		err := rows.Scan(&icao, &name, &municipality)
		if err != nil {
			log.Fatal(err)
		}


		fmt.Println(icao, name, municipality)
	}
}

