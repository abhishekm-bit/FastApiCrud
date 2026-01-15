from fastapi import APIRouter
from models.schemas import SyllabusRequest
from services.scraper import scrape
from services.embeddings import embed
from db.vector_db import store_vectors
from services.rag import retrieve
from services.gemini import generate
from db.mongo import logs

router=APIRouter()

@router.post("/generate")
def create(data:SyllabusRequest):

    scraped=scrape(data.url)


    print("Total chunks:", len(scraped))

    for i, chunk in enumerate(scraped):
        print(f"\nChunk {i+1}")
        print("Length:", len(chunk))
        print("Text:", chunk)

    # print("Scraped",scraped)
    # convert the scraped data into embedding 
    vectors=embed(scraped)

    # Stores the vectors and scraped into faiss
    store_vectors(vectors,scraped)

    # Embeeded here course ussersv from the urls t
    q_vec=embed([data.course])

    # REturns  the similar Texts t
    context=retrieve(q_vec)

    print("context",context)
    # Similar content,Course name,level ,Duration givven to gemini and generation
    result = generate(context, data.course, data.level, data.duration)

    # store request log
    logs.insert_one(data.dict())

    return {"syllabus":result}
