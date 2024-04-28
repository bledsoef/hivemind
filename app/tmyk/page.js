"use client"
import Link from "next/link";
import { MdFilterList } from "react-icons/md";
import { useEffect, useState } from "react";
import CreateTMYKModal from "@/components/CreateTMYKModal";
export default function TMYK() {
    const [showModal, setShowModal] = useState(false)
    const [games, setGames] = useState(null)
    const [showLoading, setShowLoading] = useState(true)

    useEffect(() => {
        fetchGames()
    }, [])

    const handleShowModal = () => {
        setShowModal(true)
    }
    const fetchGames = () => {
        fetch("/api/getGames/")
            .then((res) => res.json())
            .then((data) => {
                setGames(data)
                setShowLoading(false)
            }
        )
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
            {showLoading && <div>Loading</div>}
            {!showLoading && games != null && games.map((game, index) => (
                <div className="p-4 rounded-xl bg-gray-100 flex flex-row shadow-xl justify-between" key={index}>
                    <div className="flex flex-col">
                        <p className="text-4xl font-semibold">{game.game.name}</p>
                        <p>{game.user.username}</p>
                    </div>
                    <Link className="mx-2 p-3 px-4 text-xl items-center flex uppercase rounded-lg text-black font-semibold shadow-md bg-green-500" href={`/tmyk/play/${game.game.id}`}>Play</Link>
                </div>
            ))}
        </div>
      </main>
    );
  }
  