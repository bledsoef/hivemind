"use client"
import Link from "next/link";
import { MdFilterList } from "react-icons/md";
import { useState } from "react";
import CreateTMYKModal from "@/components/CreateTMYKModal";
export default function TMYK() {
    const [showModal, setShowModal] = useState(false)
    const games = [{
        title: "Football",
        author: "Fuzby",
        created: "2 days ago",
        plays: 20,
        rating: 4.5
    },{
        title: "Bright Eyes Songs",
        author: "Fuzby",
        created: "2 days ago",
        plays: 20,
        rating: 4.5
    },]
    const handleShowModal = () => {
        setShowModal(true)
    }
    return (
      <main className="flex min-h-screen flex-col py-24 px-8 bg-yellow-400">
        {showModal && <CreateTMYKModal/>}
        <div className="flex flex-row justify-between">
            <p className="text-black uppercase font-bold text-5xl">The More You Know</p>
            <div>
                <Link href={"/tmyk/create"} className="mx-2 p-3 text-xl uppercase rounded-lg text-black font-bold shadow-md bg-orange-500">Create</Link>
                <button onClick={handleShowModal} className="mx-2 p-3 text-xl uppercase rounded-lg text-black font-bold shadow-md bg-green-500">Join Live</button>
                <Link href={"/tmyk/daily"} className="mx-2 p-3 text-xl uppercase rounded-lg text-black font-bold shadow-md bg-blue-400">Daily</Link>
            </div>
        </div>
        <div className="flex flex-row justify-end mb-2 py-3">
            <button className="flex flex-row items-center px-3 bg-gray-400 rounded-lg shadow-md">
                <p className="text-xl uppercase text-black font-bold">Sort By</p>
                <MdFilterList className="flex ml-2 h-8 fill-black w-8" />
            </button>
            <input className="text-black ml-4 p-3 rounded-lg" placeholder="Search"/>
        </div>
        <div className="text-black space-y-5">
            {games.map((game, index) => (
                <div className="p-4 rounded-xl bg-gray-100 shadow-xl" key={index}>
                    <p className="text-4xl font-semibold">{game.title}</p>
                    <p>{game.author}</p>
                    <p>{game.created}</p>
                    <p>{game.plays}</p>
                    <p>{game.rating}</p>
                </div>
            ))}
        </div>
      </main>
    );
  }
  